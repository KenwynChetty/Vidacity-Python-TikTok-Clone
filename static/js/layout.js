

$(document).ready(function(){
  $('a').click(function(e){
    e.preventDefault();
  })
  //nav
  $("nav #hamburger").click(function(e){
    $('nav').toggleClass('open');
  });
  $("#primary-nav a,#ap-nav-icon-bar a").click(function(e){
    S = $(this).data('section');
    $('nav').removeClass('open');
    $("section.active").addClass('out').removeClass("active");
    $("#"+S).addClass("active");
    setTimeout(function(){$('section.out').removeClass('out');},500);
  });
  //user
  $('#settings').click(function(){
    $('#settings-panel').addClass('open');
  });
  $('#close-settings-panel').click(function(){
    $('#settings-panel').removeClass('open');
  });
  //context-menu
  $(".context-menu-btn").click(function(){
    $(this).parent().toggleClass('open');
  });
  //Accordion
  $('ul.accordion .aTitle').click(function(){
    $(this).parent('li').toggleClass('open');
  });
});