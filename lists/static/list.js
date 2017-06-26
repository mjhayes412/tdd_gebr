window.GEBR = {};
window.GEBR.initialize = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};

$(document).ready(function () {
    window.GEBR.initialize();
});
