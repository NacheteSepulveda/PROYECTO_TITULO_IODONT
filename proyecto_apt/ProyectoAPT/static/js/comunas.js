document.addEventListener('DOMContentLoaded', function() {
    const comunaSelect = document.getElementById('id_comuna');
    
    if (comunaSelect) {
        // Obtener las comunas que ya están en el select
        const comunasActuales = Array.from(comunaSelect.options).map(option => ({
            id: option.value,
            nombreComuna: option.text
        }));

        // Ordenarlas alfabéticamente
        comunasActuales
            .sort((a, b) => a.nombreComuna.localeCompare(b.nombreComuna))
            .forEach(comuna => {
                const option = document.createElement('option');
                option.value = comuna.id;
                option.textContent = comuna.nombreComuna;
                comunaSelect.appendChild(option);
            });
    }
}); 