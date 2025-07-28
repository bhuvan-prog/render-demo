function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) {
      return parseInt(uiBathrooms[i].value);
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i = 0; i < uiBHK.length; i++) {
    if (uiBHK[i].checked) {
      return parseInt(uiBHK[i].value);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "/predict_home_price";

  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function (data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    console.log(status);
  });
}

function loadLocations() {
  var url = "/get_location_names";

  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
}

function renderRadioButtons(containerId, name, count) {
  const container = document.getElementById(containerId);
  container.innerHTML = ""; // Clear old content
  for (let i = 1; i <= count; i++) {
    const input = document.createElement("input");
    input.type = "radio";
    input.name = name;
    input.id = `${containerId}-${i}`;
    input.value = i;
    if (i === 2) input.checked = true;

    const label = document.createElement("label");
    label.htmlFor = `${containerId}-${i}`;
    label.innerText = i;

    container.appendChild(input);
    container.appendChild(label);
  }
}

$(document).ready(function () {
  loadLocations();
  renderRadioButtons("uiBHK", "uiBHK", 5);
  renderRadioButtons("uiBathrooms", "uiBathrooms", 5);
});
