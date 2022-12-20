const PASS_LEN = 15;
const BLOCK_LEN = 5;

function isPrime(x) {
  for (let i = 2; i <= Math.sqrt(x); i++) {
    if (x % i === 0) {
      return false;
    }
  }
  return true;
}

function primegen(start = 1001, step = 1) {
  let i = start;
  const primes = [];
  while (primes.length < BLOCK_LEN) {
    if (isPrime(i)) {
      primes.push(i);
    }
    i += step;
  }
  return primes;
}

function keygen(P = 1001) {
  const keys = [];
  let i = 1;
  while (keys.length < BLOCK_LEN) {
    const Q = P * i + 1;
    if (isPrime(Q) && Q % P === 1) {
      keys.push(Q);
    }
    i++;
  }
  const k = Math.floor(Math.random() * BLOCK_LEN);
  return keys[k];
}

function HomoHash(a, b, x, k = 1) {
  return Math.pow(a, k * x) % b;
}

function obfuscate(x, k = [1, 1, 1, 1, 1]) {
  const obfuscatedMessage = [];
  for (let i = 0; i < x.length; i++) {
    const row = [];
    for (let j = 0; j < BLOCK_LEN; j++) {
      row.push(x[i][j] * k[j]);
    }
    obfuscatedMessage.push(row);
  }
  return obfuscatedMessage;
}

function clientHash(x, g, q, p, k = [1, 1, 1, 1, 1]) {
  const sums = [];
  const hashedSums = [];
  for (let i = 0; i < BLOCK_LEN; i++) {
    let sum = 0;
    for (let j = 0; j < x.length; j++) {
      sum += x[j][i] % p[i];
    }
    sums.push(sum % p[i]);
    hashedSums.push(HomoHash(g[i], q[i], k[i] * sums[i]));
  }
  return hashedSums;
}

function serverHash(x, g, q, p, k = [1, 1, 1, 1, 1]) {
  const sums = [];
  const hashedSums = [];
  for (let i = 0; i < BLOCK_LEN; i++) {
    let sum = 0;
    for (let j = 0; j < x.length; j++) {
      sum += x[j][i] % p[i];
    }
    sums.push(sum % p[i]);
    hashedSums.push(HomoHash(g[i], q[i], k[i] * sums[i]));
  }
  return hashedSums;
}
