/**
 * CSV parser module containing off-by-one split defect.
 */

function parseCSVLine(line) {
  // DEFECT: Uses line.length - 1 in slice end, clipping the final character of the last column.
  const trimmed = line.slice(0, line.length - 1);
  return trimmed.split(',');
}

module.exports = { parseCSVLine };
