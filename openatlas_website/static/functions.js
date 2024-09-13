$(document).ready(function() {
  $("#tags div").click(function(event) {
    $(this).toggleClass("active");
    $(".project").show();
    $(".project .tag").removeClass("active");

    var activeTags = $(".active").map(function() {
      return $(this).attr("id");
    }).get();

    if (activeTags.length > 0) {
      $(".project").each(function() {
        var projectClasses = $(this).attr("class").split(/\s+/);
        var shouldHide = !activeTags.every(function(tag) {
          return projectClasses.includes(tag);
        });

        $(this).toggle(!shouldHide);

      });
      $.each($(".active"), function() {
       $(".tag." + $(this).attr("id")).addClass("active");
      });
    } else {
      $(".project").show();
    }
  });
});

function tagClick(selection) {
  $("#" + selection).click();
}
