$(document).ready(function(){
    $(".oppic").click(function(){
      var imgWidth = $(this).css("width");
      var imgHeight = $(this).css("height");
      if (imgWidth == "250px") {
        $(this).css("width", "75%");
        $(this).removeAttr("align");            
      } else {
        $(this).css("width", "250px");
        $(this).attr("align", "left");   
      }
    });

    $(".showpic").click(function(){
      var imgWidth = $(this).css("width");
      var imgHeight = $(this).css("height");
      if (imgWidth == "125px") {
        $(this).css("width", "75%");
        $(this).removeAttr("align");            
      } else {
        $(this).css("width", "125px");
        $(this).attr("align", "left");   
      }
    });

    $(".form").toggle();
    $(".toggle_form").click(function(){
      $(".form").toggle();
      $(".toggle_form").toggle();
    });
});
