
function renderPlot(title, url) {
  $.ajax({url: url, 
          type: 'GET',
          success: function(response) {
            $('#content').append('<h2>' + title + '</h2>');
            $('#content').append('<img src="' + url + '"/>');
          },
          error: function(xhr, status) {
            window.location.replace(url);
          }        
  });
}

$(document).ready(function() {
  renderPlot('All datasets as usd', '/all-as-usd');
  renderPlot('Grams of gold per AAPL stock', '/aapl-in-gold');
  renderPlot('AAPL stock per Bitcoin', '/aapl-in-bitcoin');
});
