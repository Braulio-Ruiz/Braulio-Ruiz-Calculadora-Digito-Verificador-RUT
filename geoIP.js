//Conocer la Geolocalizacion y Organizacion a la cual pertenece la IP ingresada

// Importamos axios para hacer solicitudes HTTP a la API de ipinfo.io.
const axios = require('axios');
// Importamos readline para permitir que el usuario ingrese datos desde la consola.
const readline = require('readline');

// Configuramos una interfaz de entrada/salida para recibir datos por consola.
const rl = readline.createInterface({
    // Definimos la entrada estándar (teclado).
    input: process.stdin,
    // Definimos la salida estándar (consola).
    output: process.stdout
});

// Solicitamos al usuario que ingrese la IP que desea geolocalizar.
rl.question('\nIngrese la IP que desea geolocalizar: ', async (ip) => {
    // Token de autenticación para acceder a la API de ipinfo.io.
    const token = '38d231550b9d03';

    // Construimos la URL para hacer la solicitud HTTP, usando la IP ingresada y el token.
    const url = `https://ipinfo.io/${ip}?token=${token}`;

    try {
        // Realizamos una solicitud HTTP GET a la API usando axios.
        const response = await axios.get(url);

        // Obtenemos los datos de la respuesta de la API en formato JSON.
        const data = response.data;

        // Mostramos los datos de la IP de manera didáctica en la consola.
        console.log(`\n--- Información de la IP: ${ip} ---\n`);
        console.log(`🌍 Ubicación: ${data.city}, ${data.region}, ${data.country}`);
        console.log(`📍 Coordenadas: ${data.loc}`);
        console.log(`🏢 Organización: ${data.org}`);
        console.log(`🕒 Zona Horaria: ${data.timezone}\n`);

    } catch (error) {
        // Si ocurre un error (como una IP no válida o un problema de red), mostramos un mensaje de error detallado en la consola.
        console.error('Error al obtener la información de la IP: \n', error.message);

    } finally {
        // Cerramos la interfaz de lectura para finalizar el programa.
        rl.close();
    }
});
