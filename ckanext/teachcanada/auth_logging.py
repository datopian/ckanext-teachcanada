"""
Authentication logging plugin for debugging login issues.
Adds comprehensive logging throughout the authentication flow.
"""
import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import g, request
from flask import session

log = logging.getLogger(__name__)


class AuthLoggingPlugin(plugins.SingletonPlugin):
    """
    Plugin that adds detailed logging to the authentication process.
    This helps identify why login credentials might be failing.
    """
    plugins.implements(plugins.IAuthenticator)
    plugins.implements(plugins.IBlueprint)

    def authenticate(self, identity):
        """
        Called to authenticate a user with their credentials.
        This is the main authentication method that validates credentials.

        Returns: User object if authentication succeeds, None otherwise
        """
        from ckan.model import User

        log.info("@"*80)
        log.info("AUTH_LOG: authenticate() called - VALIDATING CREDENTIALS")
        log.info(f"AUTH_LOG: Identity keys: {list(identity.keys()) if identity else 'None'}")

        if identity:
            login = identity.get('login', '')
            password = identity.get('password', '')
            log.info(f"AUTH_LOG: Attempting to authenticate user: '{login}'")

            # Check if password is present (but don't log it)
            if 'password' in identity:
                password_length = len(password)
                log.info(f"AUTH_LOG: Password provided, length: {password_length}")
            else:
                log.warning("AUTH_LOG: WARNING - No password in identity!")

            # Try to find user by name
            user_obj = User.by_name(login)
            if user_obj:
                log.info(f"AUTH_LOG: User found by name: {user_obj.name}")
                log.info(f"AUTH_LOG: User is active: {user_obj.is_active}")
                log.info(f"AUTH_LOG: User email: {user_obj.email}")
            else:
                log.warning(f"AUTH_LOG: User NOT found by name '{login}', trying email...")
                user_obj = User.by_email(login)
                if user_obj:
                    log.info(f"AUTH_LOG: User found by email: {user_obj.name}")
                    log.info(f"AUTH_LOG: User is active: {user_obj.is_active}")
                else:
                    log.error(f"AUTH_LOG: ERROR - User '{login}' NOT FOUND in database!")
                    log.info("@"*80)
                    return None

            # Validate password
            if user_obj:
                password_valid = user_obj.validate_password(password)
                log.info(f"AUTH_LOG: Password validation result: {password_valid}")

                if not password_valid:
                    log.error("AUTH_LOG: ERROR - PASSWORD VALIDATION FAILED!")
        else:
            log.warning("AUTH_LOG: WARNING - Identity is None!")

        # Let CKAN's default authenticator handle the actual authentication
        # We return None to pass control to the next authenticator in the chain
        log.info("AUTH_LOG: Passing to next authenticator in chain (CKAN default)")
        log.info("@"*80)
        return None

    def identify(self):
        """
        Called at the start of every request to identify the user.
        This is where we can log authentication state.
        """
        log.info("="*80)
        log.info("AUTH_LOG: identify() called")
        log.info(f"AUTH_LOG: Request path: {request.path}")
        log.info(f"AUTH_LOG: Request method: {request.method}")
        log.info(f"AUTH_LOG: Session keys: {list(session.keys())}")

        # Check if user is in session
        if 'user' in session:
            log.info(f"AUTH_LOG: User in session: {session.get('user')}")
        else:
            log.info("AUTH_LOG: No user in session")

        # Check Flask-Login user
        if hasattr(g, 'user'):
            log.info(f"AUTH_LOG: g.user: {g.user}")
        else:
            log.info("AUTH_LOG: No g.user set")

        if hasattr(g, 'userobj'):
            log.info(f"AUTH_LOG: g.userobj: {g.userobj}")
        else:
            log.info("AUTH_LOG: No g.userobj set")

        log.info("="*80)

    def login(self):
        """
        Called when a user logs in successfully.
        """
        log.info("*"*80)
        log.info("AUTH_LOG: login() called - USER LOGGED IN SUCCESSFULLY")
        log.info(f"AUTH_LOG: Session after login: {dict(session)}")
        if hasattr(g, 'user'):
            log.info(f"AUTH_LOG: Logged in user: {g.user}")
        if hasattr(g, 'userobj'):
            log.info(f"AUTH_LOG: User object: {g.userobj}")
        log.info("*"*80)

    def logout(self):
        """
        Called when a user logs out.
        """
        log.info("*"*80)
        log.info("AUTH_LOG: logout() called - USER LOGGING OUT")
        log.info(f"AUTH_LOG: Session before logout: {dict(session)}")
        log.info("*"*80)

    def abort(self, status_code, detail, headers, comment):
        """
        Called when an authorization check fails.
        """
        log.warning("!"*80)
        log.warning("AUTH_LOG: abort() called - AUTHORIZATION FAILED")
        log.warning(f"AUTH_LOG: Status code: {status_code}")
        log.warning(f"AUTH_LOG: Detail: {detail}")
        log.warning(f"AUTH_LOG: Comment: {comment}")
        log.warning(f"AUTH_LOG: Request path: {request.path}")
        log.warning("!"*80)
        return (status_code, detail, headers, comment)

    def get_blueprint(self):
        """
        Register a blueprint to intercept login POST requests.
        """
        from flask import Blueprint

        blueprint = Blueprint('auth_logging', __name__)

        @blueprint.before_app_request
        def log_before_request():
            """Log every request, with special attention to login attempts."""
            if request.path == '/user/login' and request.method == 'POST':
                log.info("#"*80)
                log.info("AUTH_LOG: LOGIN FORM SUBMITTED")
                log.info(f"AUTH_LOG: Request form keys: {list(request.form.keys())}")

                # Log username (but not password)
                username = request.form.get('login', '')
                log.info(f"AUTH_LOG: Username/email submitted: '{username}'")

                # Check if password field is present (but don't log the value)
                if 'password' in request.form:
                    password_length = len(request.form.get('password', ''))
                    log.info(f"AUTH_LOG: Password field present, length: {password_length}")
                else:
                    log.warning("AUTH_LOG: WARNING - No password field in form submission!")

                # Log remember me checkbox
                remember = request.form.get('remember', '')
                log.info(f"AUTH_LOG: Remember me: {remember}")

                log.info("#"*80)

        return blueprint
