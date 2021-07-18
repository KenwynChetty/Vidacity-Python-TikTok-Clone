	//user
	$('#settings').click(function(){
        $('#settings-panel').addClass('open');
      });
      $('#close-settings-panel').click(function(){
        $('#settings-panel').removeClass('open');
      });
      
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
                $("#likebtn" + id).html('<svg xmlns="http://www.w3.org/2000/svg"  width="1.5em" height="1.5em" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"  style="z-index:100; font-size:33px"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg>');
                $("#likebtn" + id).css("color", "red");

              } else {
                $("#likebtn" + id).html('<svg xmlns="http://www.w3.org/2000/svg"  width="1.5em" height="1.5em" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"  style="z-index:100; font-size:33px"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg>');
                $("#likebtn" + id).css("color", "white");
              }
            },
          });
          document.location.reload(true)
        });