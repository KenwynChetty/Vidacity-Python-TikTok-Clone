$(".like").click(function (e) {
    var id = this.id;
    var href = $(".like").find("a").attr("href");
    e.preventDefault();

    $.ajax({
      url: href,
      data: {
        likeId: id,
      },
      success: function (response) {
        if (response.liked) {
          $("#likebtn" + id).html("Unlike");
          $("#likebtn" + id).css("color", "red");
        } else {
          $("#likebtn" + id).html("Like");
          $("#likebtn" + id).css("color", "green");
        }
      },
    });
  });