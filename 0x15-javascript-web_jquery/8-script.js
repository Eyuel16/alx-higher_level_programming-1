$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  // console.log(data.results);
  $.each(data.results, function (index, element) {
    $('#list_movies').append('<li>' + element.title + '</li');
  });
});
