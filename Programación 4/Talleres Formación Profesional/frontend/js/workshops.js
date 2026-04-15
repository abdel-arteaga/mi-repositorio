console.log("workshops.js cargado");



// CAMBIAR ESTA URL CUANDO SEA NECESARIO

const API_URL = "http://localhost:5000/workshops";



const table = document.getElementById("workshopsTable");



fetch(API_URL)

  .then(response => response.json())

  .then(data => {

    table.innerHTML = "";

    data.forEach(workshop => {

      table.innerHTML += `

        <tr>

          <td>${workshop.name}</td>

          <td>${workshop.date}</td>

          <td>${workshop.time}</td>

          <td>${workshop.place}</td>

          <td>

            <button class="btn btn-success btn-sm"

              onclick="registerWorkshop(${workshop.id})">

              Registrarse

            </button>

          </td>

        </tr>

      `;

    });

  });



function registerWorkshop(id) {

  fetch(`${API_URL}/${id}/register`, { method: "POST" })

    .then(() => alert("✅ Registro exitoso"))

    .catch(() => alert("❌ Error al registrarse"));

}