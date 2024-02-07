$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (response) {
      $('div#hello').text(response.hello);
    },
    error: function (xhr, status, error) {
      console.error('Error fetching character name:', error);
    }
  });
});
