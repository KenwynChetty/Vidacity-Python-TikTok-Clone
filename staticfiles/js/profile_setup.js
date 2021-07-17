function upload(){
    var fileinput = document.getElementById("document-upload");
    var image = new SimpleImage(fileinput);
    var canvas = document.getElementById("can");
    image.drawTo(canvas)
  }