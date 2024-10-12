// filtro.js

function removeAccents(str) {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function filterServices() {
    const searchInput = removeAccents(document.getElementById("searchInput").value.toLowerCase());
    const universitySelect = removeAccents(document.getElementById("universitySelect").value.toLowerCase());
    const treatmentSelect = removeAccents(document.getElementById("treatmentSelect").value.toLowerCase());
    const servicesList = document.getElementById("servicesList").children;

    for (let i = 0; i < servicesList.length; i++) {
        const servicio = servicesList[i];
        const servicioText = removeAccents(servicio.innerText.toLowerCase());
        const servicioUniversity = removeAccents(servicio.getAttribute("data-university").toLowerCase());
        const servicioTreatment = removeAccents(servicio.getAttribute("data-treatment").toLowerCase());

        // Verificar coincidencias
        const matchesSearch = servicioText.includes(searchInput);
        const matchesUniversity = !universitySelect || servicioUniversity.includes(universitySelect);
        const matchesTreatment = !treatmentSelect || servicioTreatment.includes(treatmentSelect);

        // Mostrar u ocultar servicio
        servicio.style.display = (matchesSearch && matchesUniversity && matchesTreatment) ? "" : "none";
    }
}

// Agregar event listeners
document.getElementById("searchInput").addEventListener("keyup", filterServices);
document.getElementById("universitySelect").addEventListener("change", filterServices);
document.getElementById("treatmentSelect").addEventListener("change", filterServices);

// Llamar a filterServices() al cargar la página
document.addEventListener("DOMContentLoaded", filterServices);
