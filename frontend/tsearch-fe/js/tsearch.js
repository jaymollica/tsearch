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
        console.log('did it');
      }
    };
  });
})(this, jQuery);