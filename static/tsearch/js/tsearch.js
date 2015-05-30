'use strict';

(function(window, $) {

  $(document).ready(function() {

    $('.color').on("click",function() {
      $('.color').removeClass('selected');   
      $(this).addClass('selected');
      var decade = $(event.currentTarget).data('color');
      addSelection('decade', decade);
    });

    $('.medium').on("click",function() {
      $('.medium').removeClass('selected');    
      $(this).addClass('selected');
      var medium = $(event.currentTarget).data('medium');
      addSelection('medium', medium);
    });

    $('.country').on("click",function() {
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

    $(".close").on("click touchstart",function() {
      $('.color').removeClass('selected');
      $('.medium').removeClass('selected');
      $('.country').removeClass('selected');
      selectedElements = [];
    });

    function createGallery(filters) {

      var url = "/backend/gallery";

      var decade = filters.decade;
      var medium = filters.medium;
      var country = filters.country;

      $.ajax({
        url: url,
        data: {decade: decade, medium: medium, country:country}
      }).done(function(data) {
        $("#gallery").empty();
        console.log(data);
        $('#gallery-container').modal('toggle');

        if(data.length > 0) {
          $.each(data, function(i) {
            var artist = this.fields.artist;
            var image_url = this.fields.url;
            var title = this.fields.title;

            $('<div class="item"><img src="'+image_url+'"><div class="carousel-caption"><i>'+title+'</i><br>'+artist+'</div>   </div>').appendTo('.carousel-inner');
            $('<li data-target="#carousel-example-generic" data-slide-to="'+i+'"></li>').appendTo('.carousel-indicators')

            $('.item').first().addClass('active');
            $('.carousel-indicators > li').first().addClass('active');
            $('#carousel-example-generic').carousel();

          });
        }
        else {
          $("<div><p>No Results!  Try Again...</p></div>").appendTo('.carousel-inner');
        }
      });

    }

  });
})(this, jQuery);