async function main() {
  const MotoCarbonToken = await ethers.getContractFactory("MotoCarbonToken");

  const contrato = await MotoCarbonToken.deploy();

  await contrato.waitForDeployment();

  console.log("MotoCarbonToken desplegado en:", await contrato.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
