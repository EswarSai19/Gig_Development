const { parseStringPromise } = require("xml2js");

async function fetchImageKeys() {
  try {
    const response = await fetch(
      // "https://piy8oxo2v3.execute-api.ap-south-1.amazonaws.com/Sandbox/fantomtestimages"
      "https://pl3jxdg8e2.execute-api.ap-south-1.amazonaws.com/Sandbox/homepage-logos"
    );
    const cdnBaseUrl = "https://dxcln6pws6tir.cloudfront.net/";
    const text = await response.text();

    // Parse XML to JSON
    const result = await parseStringPromise(text);

    // Extract keys
    const keys = result.ListBucketResult.Contents.map((item) => item.Key[0]);

    console.log(keys); // Output the extracted keys
    for (let i = 0; i < keys.length; i++) {
      console.log(cdnBaseUrl + keys[i]);
    }
    return keys;
  } catch (error) {
    console.error("Error fetching image keys:", error);
  }
}

fetchImageKeys();

// console.log(cdnBaseUrl + imgArr[0]); // Output the first image URL
