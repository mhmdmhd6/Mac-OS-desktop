$(document).ready(function() {
    function fetchData() {
      $.ajax({
        url: "/api/data",
        method: "GET",
        success: function(data) {
          $('.battery__text').text(data.battery);
          $('.wifi').text(data.wifi);
          $('.bluetooth').text(data.bluetooth);
        }
      });
    }
    
    fetchData();
    setInterval(fetchData, 15000);
  });
  