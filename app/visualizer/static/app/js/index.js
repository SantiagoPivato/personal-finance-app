/**
 * GLOBAL VARIABLES
 */
let chartCounter = 0;
let charts = {};


/**
 * Async functions
 */
const getVariableValues = async (variable, from, to) => {
  const url = `/variableValuesBCRA/${variable}?from=${from}&to=${to}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    return json;
  } catch (error) {
    console.error(error.message);
    return false;
  }
}

/**
 * Event handlers
 */
const newChartHandler = () => {
  const variable = document.getElementById("new-chart-variable").value;
  const from_date = document.getElementById("new-chart-from-date").value;
  const to_date = document.getElementById("new-chart-to-date").value;

  if(variable == ""){
    showError("A Variable must be selected."); 
    return;
  }else if(from_date == ""){
    showError("A From Date must be selected.");
    return;
  }else if(to_date == ""){
    showError("A To Date must be selected."); 
    return;
  }else if(from_date > to_date){
    showError("The From Date can not be grater than the To Date.");
    return;
  }

  getVariableValues(variable, from_date, to_date).then(response => {
    const title = document.querySelector("#new-chart-variable").selectedOptions[0].text;
    
    addChartCard(title);
    charts[chartCounter] = setChart(
      "chart-" + chartCounter,
      response.data.map(row => row.datetime.slice(0,10)),
      response.data.map(row => row.value),
      title
    );
    
    
    chartCounter++;
  });
}

const removeChartHandler = (chartNumber) => {
  charts[chartNumber].destroy();
  delete charts[chartNumber];
  const chartCard = document.getElementById("chart-card-" + chartNumber);
  chartCard.parentElement.remove();
}


/**
 * AUX
 */
const addChartCard= (title) => {
  const innerHTML = `<div class="card text-center" id="chart-card-${chartCounter}">
                    <div class="card-body">
                        <h5 class="card-title">${title}</h5>
                        <div><canvas id="chart-${chartCounter}"></canvas></div>
                        <a href="#" class="btn btn-danger mt-3" onclick="removeChartHandler(${chartCounter})">Remove</a>
                    </div>
                </div>`;

  const chartCardContainer = document.createElement("div");
  chartCardContainer.className = "col-md-6 mb-3"; 
  chartCardContainer.innerHTML = innerHTML; 

  const newChartCard = document.getElementById("new-chart-card");
  newChartCard.parentElement.insertAdjacentElement("beforebegin", chartCardContainer)
}


const setChart = (id, labels, data, title) => {
  return new Chart(
    document.getElementById(id),
    {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: title,
            data: data
          }
        ]
      },
      options:{
        plugins: {
          title: {
              display: true,
              text: title
          }
      }
      }
    }
  );
}

//Executed when document is ready
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("new-chart-btn").addEventListener("click", newChartHandler);
});