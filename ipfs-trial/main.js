require('dotenv').config();
const AWS = require('aws-sdk');
const  s3 = new AWS.S3({endpoint: 'https://s3.filebase.com', signatureVersion: 'v4' });

/*Uploading Files */
function Upload(bucket, name, content) {
    var params = {
        Body: content,
        Bucket: bucket,
        Key: name,
        ContentType: 'application/json'
    };
    s3.putObject(params, function(error, data) {
        if (error) {
          console.error(error);
        } else {
          console.log('Successfully uploaded file' + name + ":" + bucket);
        }
    });
}

/*Downloading files */
function Download(bucket, key, callback) {
    var params = {
      Key: key,
      Bucket: bucket
    };
    try {
      s3.getObject(params, function(error, data) {
        if (error) {
          console.log("Error while reading file " + key + ":" + bucket);
          return callback("Error!");
        } else {
          console.log("Returning contents from " + key + ":" + bucket);
          return callback(Buffer.from(data.Body, 'utf8').toString());
        }
      });
    } catch (error) {
      console.error(error);
      return callback("Error!");
    }
  }

Upload('ipfs-trial-01', "user.json", "user.json");


