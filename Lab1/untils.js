function mapToPlot(yValue){

    const phase = {
        x: epsValues,
        y: yValue.map(y => y.phase),
        type: 'scatter'
    }
    const angle = {
        x: epsValues,
        y: yValue.map(y => y.angle),
        type: 'scatter'
    }
    return {phase, angle}
}