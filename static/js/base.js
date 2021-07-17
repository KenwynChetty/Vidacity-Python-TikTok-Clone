function fakesearch(time){
  $("#search-bar").addClass("loading");
  $("#search-btn").addClass("loading");
  setTimeout(function(){
    $("#search-bar").removeClass('active loading');
    $("#search-btn").removeClass("loading");
    $("nav,#settings").removeClass("hide");
  },time);
}

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
  //search
  $("#search-bar #search-btn").click(function(e){
    if($("#search-bar").hasClass('active')){
      e.preventDefault();
      fakesearch(2000);
      $.ajax({
        type: 'POST',
        url: '{% url "search_posts" %}',
        data: {
          context: $('search').val(),
          csrfmiddlewaretoken: $('{% csrf_token %}').val(),
          action: 'post'
        },});
    }else{
      e.preventDefault();
      $("#search-bar").addClass("active");
      $("#search-input").focus();
      $("nav,#settings").removeClass("open").addClass("hide");
    }
  });
  $("#close-search").click(function(e){
    $("#search-bar").removeClass("active");
    $("#search-btn").removeClass("loading");
     $("nav,#settings").removeClass("hide");
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