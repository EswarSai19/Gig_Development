// Define the API URL and CloudFront base URL
const apiUrl = "https://example.com/api/get-image-key"; // Replace with your API endpoint
const cloudfrontBaseUrl = "https://dh156u3f22681.cloudfront.net/"; // Replace with your CloudFront base URL

// Function to fetch and display the image
async function fetchAndDisplayImage() {
  try {
    // Make the API call
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error("Failed to fetch image data from API");
    }

    // Parse the response
    const data = await response.json();
    const objectKey = data.Key; // Fetching Key from the API response

    if (!objectKey) {
      throw new Error("Object key not found in API response");
    }

    // Construct the image URL
    const imageUrl = cloudfrontBaseUrl + objectKey;

    // Update the image source and display it
    const imageElement = document.getElementById("dynamic-image");
    imageElement.src = imageUrl;
    imageElement.style.display = "block";
  } catch (error) {
    // Handle errors
    document.getElementById("error-message").textContent = error.message;
  }
}

// Call the function when the page loads
window.onload = fetchAndDisplayImage;
