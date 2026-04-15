console.log("admin.js cargado");



const API_URL = "http://localhost:5000/workshops";



const table = document.getElementById("adminTable");

const form = document.getElementById("workshopForm");



function loadWorkshops() {

  fetch(API_URL)

    .then(res => res.json())

    .then(data => {

      table.innerHTML = "";

      data.forEach(w => {

        table.innerHTML += `

          <tr>

            <td>${w.name}</td>

            <td>${w.date}</td>

            <td>

              <button class="btn btn-danger btn-sm"

                onclick="deleteWorkshop(${w.id})">

                Eliminar

              </button>

            </td>

          </tr>

        `;

      });

    });

}



form.addEventListener("submit", e => {

  e.preventDefault();



  const workshop = {

    name: name.value,

    description: description.value,

    date: date.value,

    time: time.value,

    place: place.value,

    category: category.value

  };



  fetch(API_URL, {

    method: "POST",

    headers: { "Content-Type": "application/json" },

    body: JSON.stringify(workshop)

  })

  .then(() => {

    alert("✅ Taller creado");

    form.reset();

    loadWorkshops();

  });

});



function deleteWorkshop(id) {

  fetch(`${API_URL}/${id}`, { method: "DELETE" })

    .then(() => loadWorkshops());

}



loadWorkshops();