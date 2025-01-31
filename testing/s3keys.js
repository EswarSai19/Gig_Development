const { parseStringPromise } = require("xml2js");

async function fetchImageKeys() {
  try {
    const response = await fetch(
      "https://piy8oxo2v3.execute-api.ap-south-1.amazonaws.com/Sandbox/fantomtestimages"
    );
    const text = await response.text();

    // Parse XML to JSON
    const result = await parseStringPromise(text);

    // Extract keys
    const keys = result.ListBucketResult.Contents.map((item) => item.Key[0]);

    console.log(keys); // Output the extracted keys
    return keys;
  } catch (error) {
    console.error("Error fetching image keys:", error);
  }
}

fetchImageKeys();
