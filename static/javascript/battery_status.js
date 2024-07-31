$(document).ready(function () {
  function fetchData() {
    $.ajax({
      url: "/api/data",
      method: "GET",
      success: function (data) {
        $('.battery__text').text(data.battery);
        $('.wifi').text(data.wifi);
        $('.bluetooth').text(data.bluetooth);
        $('.charging-status').text(data.charging);
        $('.time-left').text(data.time_left);
      }
    });
  }

  fetchData();
  setInterval(fetchData, 15000);
});
