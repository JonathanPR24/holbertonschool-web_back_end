/* promise need a function to work */
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an asynchronous operation (e.g., an API call)
    setTimeout(() => {
      // Simulate a successful response
      resolve("API response data");

      // Simulate an error
      // reject(new Error("API request failed"));
    }, 1000); // Simulate a delay of 1 second
  });
}
