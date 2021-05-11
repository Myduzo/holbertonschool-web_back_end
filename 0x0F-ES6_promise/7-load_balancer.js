export default async function loadBalancer(chinaDownload, USDownload) {
  const promises = [chinaDownload, USDownload];
  return Promise.race(promises).then((val) => val);
}
