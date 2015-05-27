'use-strict';

(function(window, $) {

  $(document).ready(function() {

    $('.color').click(function() {
      $('.color').removeClass('selected');   
      $(this).addClass('selected');
      var color = $(event.currentTarget).data('color');
      addSelection('color', color);
    });

    $('.medium').click(function() {
      $('.medium').removeClass('selected');    
      $(this).addClass('selected');
      var medium = $(event.currentTarget).data('medium');
      addSelection('medium', medium);
    });

    $('.country').click(function() {
      $('.country').removeClass('selected');   
      $(this).addClass('selected');
      var country = $(event.currentTarget).data('country');
      addSelection('country', country);
    });

    var selectedElements = [];

    function addSelection(key, val) {
      
      selectedElements[key] = val;

      var length = Object.keys(selectedElements).length;

      if (length === 3) {
        createGallery(selectedElements);
      }
    };

    function createGallery(filters) {

      var url = "/php/get_gallery.php";

      $.ajax({
        type: "POST",
        url: url,
        data: {filters: filters},
      }).done(function(data) {
        $("#gallery").empty();

        $.each(data, function(i) {
          var artist = this.artist;
          var image_url = this.image_url;
          var title = this.title;

          $('<div class="item"><img src="'+image_url+'"><div class="carousel-caption">'+title+'<br>'+artist+'</div>   </div>').appendTo('.carousel-inner');
          $('<li data-target="#carousel-example-generic" data-slide-to="'+i+'"></li>').appendTo('.carousel-indicators')

          $('.item').first().addClass('active');
          $('.carousel-indicators > li').first().addClass('active');
          $('#carousel-example-generic').carousel();

        });
      });

    }

  });
})(this, jQuery);