/**
 * Gateway request handler module containing null property access defect.
 */

function handleRequest(req) {
  // DEFECT: Accesses req.headers['authorization'] directly without null checking req or req.headers.
  // When req.headers is undefined, throws TypeError: Cannot read properties of undefined.
  const auth = req.headers['authorization'];
  const parts = auth.split(' ');
  return {
    authenticated: true,
    scheme: parts[0],
    token: parts[1]
  };
}

module.exports = { handleRequest };
