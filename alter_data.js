const mysql = require('mysql');
const faker = require('faker');

const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "e_commerce"
});

connection.connect();
const updateProductsWithBrand = () => {
    for (let product_id = 1; product_id <= 2500; product_id++) {
      const fetchSql = 'SELECT attributes FROM products WHERE product_id = ?';
  
      connection.query(fetchSql, [product_id], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
          // Parse the existing attributes and add a brandName
          let attributes = JSON.parse(results[0].attributes);
          attributes.brandName = faker.company.companyName(); // Generate and add brand attribute
  
          // Update the product with the new attributes
          const updateSql = `UPDATE products SET attributes = ? WHERE product_id = ?`;
          connection.query(updateSql, [JSON.stringify(attributes), product_id], (updateErr) => {
            if (updateErr) throw updateErr;
            console.log(`Product ID ${product_id} updated with new brandName.`);
          });
        }
      });
    }
  };
  
  updateProductsWithBrand();
// Optional: Close the connection if you are done with all operations
// Consider the asynchronous nature of Node.js when deciding where to place connection.end();
// It might be more appropriate to close the connection after confirming all updates are complete,
// which could be complex due to the asynchronous loops.