$(document).ready(()=>{

  $(".ttoggle").click(()=>{
    $('#tgl').toggleClass('fa-bars fa-times');
  })

  $(".ttoggle2").click(()=>{
    $('#tgl2').toggleClass('fa-bars fa-times');
  })

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