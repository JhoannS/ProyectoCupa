const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',      
  user: 'root',     
  password: '',
  database: 'cupaBurger' 
});

// Función para mostrar el resultado en la página
function mostrarResultadoEnPagina(rowCount) {
    const rowCountElement = document.getElementById('rowCount');
    rowCountElement.textContent = rowCount;
  }
  
  // Conectar a la base de datos
  connection.connect((err) => {
    if (err) {
      console.error('Error al conectar a la base de datos:', err.message);
      return;
    }
  
    // Consulta SQL para contar las filas en una tabla (reemplaza 'mi_tabla' por el nombre de tu tabla)
    const query = 'SELECT COUNT(*) AS rowCount FROM mi_tabla';
  
    // Ejecutar la consulta
    connection.query(query, (err, results) => {
      if (err) {
        console.error('Error al contar las filas:', err.message);
      } else {
        const rowCount = results[0].rowCount;
        mostrarResultadoEnPagina(rowCount); // Mostrar el resultado en la página
      }
  
      // Cerrar la conexión a la base de datos
      connection.end((err) => {
        if (err) {
          console.error('Error al cerrar la conexión:', err.message);
        }
      });
    });
  });
  