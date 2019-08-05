var initPage = function() {
  console.log('in init, django.jQuery=', django.jQuery);
  if (django.jQuery) {
    
    (function($) {
      if ($) {
        $('.register').on('click', function (event) {
          event.preventDefault();
          console.log('registering pet');
          var button = $(this);
          var url = button.data('register_url');
          var petId = button.data('pet_id');

          $.ajax({
            method: "POST",
            url: url,
            data: {pet_id: petId}
          })
            .done(function (result) {
              console.log('Ajax call to register pet succeeded: ', result);
              location.reload();
            })
            .catch(function (result) {
              console.log('Ajax call to register pet failed: ', result);
            });
        });
      }
    })(django.jQuery);
    
  } else {
    setTimeout(initPage, 300);
  }
};

initPage();
