$(document).ready(()=>{

  $(".ttoggle").click(()=>{
    $('#tgl').toggleClass('fa-bars fa-times');
  })

  // Remove the manual click handler for ttoggle2 - let Bootstrap events handle it
  // Listen for Bootstrap dropdown events to sync the icon
  $('.ttoggle2').parent('.dropdown').on('shown.bs.dropdown', function() {
    // When dropdown opens, ensure icon is X
    $('#tgl2').removeClass('fa-bars').addClass('fa-times');
  });

  $('.ttoggle2').parent('.dropdown').on('hidden.bs.dropdown', function() {
    // When dropdown closes, ensure icon is bars
    $('#tgl2').removeClass('fa-times').addClass('fa-bars');
  });

  $("#cancel").click((e)=> {
    e.preventDefault();
    $("#searchicon").css("display", "block")
    $("#search").css("display", "none")
  })

  $("#searchicon").click(()=> {
    $("#searchicon").css("display", "none")
    $("#search").css("display", "block")
  })

  $('.dropdown.keep-open').on({
    "shown.bs.dropdown": function() { this.closable = false; },
    "click":             function() { this.closable = true; },
    "hide.bs.dropdown":  function() { return this.closable; }
  });
})