$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      response.films.forEach(function (movie) {
        $.ajax({
          type: 'GET',
          url: movie,
          success: function (response2) {
            $('#list_movies').append('<li>' + response2.title + '</li>');
          }
        });
      });
    },
    error: function (xhr, status, error) {
      console.error('Error fetching character name:', error);
    }
  });
});
