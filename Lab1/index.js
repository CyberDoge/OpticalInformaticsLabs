let ALFA = 1, BETA = 1, a = -1, b = 1, p = -1, q = 1, m = 1000, n = 1000;
const kArray = Array.apply(null, {length: n - 1}).map(Number.call, Number);
let epsValues = math.range(p, q, (q - p) / m).toArray()
let h_x = (b - a) / n;

function f_x(x) {
    return math.evaluate(`e^(i*${BETA}*${x})`);
}

function K_eps_x(eps, x) {
    // return math.complex(math.evaluate(`e^(-${ALFA} * abs(${x} + i*${eps}))`));
    return math.evaluate(`e^(-${ALFA} * abs(${x} + i*${eps}))`);
}

function x_k(k) {
    return a + k * h_x;
}

function findF_eps(eps) {
    return kArray.reduce((prevSum, k) => {
        return math.sum(prevSum, math.multiply(
            K_eps_x(eps, x_k(k)), f_x(x_k(k)) /*const*/, h_x  /*const*/)
        )
    }, 0)
}

function renderPrimary() {

    const values = epsValues.map(x => {
        const f = f_x(x);
        return ({
            phase: math.abs(f),
            angle: math.atan2(f.im, f.re)
        })
    })
    const {phase, angle} = mapToPlot(values)

    Plotly.newPlot('primary_phase', [phase])
    Plotly.newPlot('primary_angle', [angle])
}

function renderKernel() {
    const xValues = math.range(a, b, (b - a) / n).toArray();
    const value = epsValues.map(e => {
        const fArray = xValues.map(x => K_eps_x(e, x));
        return ({
            phases: fArray.map(f => math.abs(f)),
            angle: fArray.map(f => math.atan2(f.im, f.re))
        })
    })
    const phases = {z: value.map(phases => phases.phases), type: "surface"}
    const angles = {z: value.map(angle => angle.angle), type: "surface"}
    console.table(phases)
    Plotly.newPlot('kernel_phase', [phases])
    Plotly.newPlot('kernel_angle', [angles])
}

function renderResult() {
    const yValues = epsValues.map((eps, index) => {
        const res = findF_eps(eps);
        return {
            phase: math.abs(res),
            angle: math.atan2(res.im, res.re)
        }
    })

    const {phase, angle} = mapToPlot(yValues)

    Plotly.newPlot('phase', [phase])
    Plotly.newPlot('angle', [angle])
    console.log("ready")
}

function draw() {
    try {
        document.getElementById("aNum").onchange = e => {
            a = +e.target.value;
            h_x = (b - a) / n;
            renderResult()
        }

        document.getElementById("bNum").onchange = e => {
            b = +e.target.value;
            h_x = (b - a) / n;
            renderResult()
        }
        document.getElementById("pNum").onchange = e => {
            p = +e.target.value;
            epsValues = math.range(p, q, (q - p) / m).toArray()
            renderResult()
        }
        document.getElementById("qNum").onchange = e => {
            q = +e.target.value;
            epsValues = math.range(p, q, (q - p) / m).toArray()
            renderResult()
        }
        // [0, 1, ..., n - 1]
        // const com = math.complex(2.5, 3.2)
        // const foo = math.multiply(10, com)
        // console.log(foo)
        // renderPrimary();
        // renderKernel();
        renderResult();
        // evaluate the expression repeatedly for different values of x

    } catch (err) {
        console.error(err)
        alert(err)
    }
}
