function initMap() {
  var map = new google.maps.Map(document.getElementById('map-container'), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
    gestureHandling: 'greedy',  // Enable gesture handling for map rotation
  });

  var infoWindow = new google.maps.InfoWindow({ map: map });
  var userMarker;

  // Try HTML5 geolocation.
  const YOUR_DESTINATION_LATITUDE = 3.8352606850754616;
  const YOUR_DESTINATION_LONGITUDE = 11.50470068460044;

  if (navigator.geolocation) {
    // Update user's position every 5 seconds
    navigator.geolocation.watchPosition(function (position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      // Update the map center
      map.setCenter(pos);

      // Update the user's marker or create a new one
      if (userMarker) {
        userMarker.setPosition(pos);
      } else {
        userMarker = new google.maps.Marker({
          position: pos,
          map: map,
          title: 'Your Position'
        });
      }

      // Request directions from user's location to the destination
      var directionsService = new google.maps.DirectionsService();
      var directionsDisplay = new google.maps.DirectionsRenderer();
      directionsDisplay.setMap(map);

      var request = {
        origin: pos,
        destination: { lat: YOUR_DESTINATION_LATITUDE, lng: YOUR_DESTINATION_LONGITUDE },
        travelMode: 'DRIVING'
      };

      directionsService.route(request, function (result, status) {
        if (status == 'OK') {
          directionsDisplay.setDirections(result);
        } else {
          console.error('Directions request failed due to ' + status);
        }
      });

    }, function () {
      handleLocationError(true, infoWindow, map.getCenter());
    });

    // Add deviceorientation event listener for orientation
    window.addEventListener('deviceorientation', handleOrientation);
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }

}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
    'Error: The Geolocation service failed.' :
    'Error: Your browser doesn\'t support geolocation.');
}

function toggleFullscreen() {
  var infoContainer = document.getElementById('info-container');
  infoContainer.classList.toggle('fullscreen');
}
