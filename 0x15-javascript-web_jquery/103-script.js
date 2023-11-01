$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const api = 'https://www.fourtonfish.com/hellosalut/?';

    $.get(api, { lang: $('INPUT#language_code').val() }, function (data) {
      $('DIV#hello').html(data.hello);
    });
  }
});
