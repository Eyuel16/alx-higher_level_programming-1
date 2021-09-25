$(function () {
  $('#btn_translate').click(function () {
    const codes = $('#language_code').val();
    // console.log(codes);
    $.get('https://fourtonfish.com/hellosalut/?lang=' + codes, function (data, status) {
      if (status === 'success') {
        $('#hello').text(data.hello);
        // console.log(data.hello);
      }
    });
  });
});
