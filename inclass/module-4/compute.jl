#!/usr/bin/env julia

import JSON

## Welcome
jobid=get(ENV,"SLURM_JOB_ID","0")
stepid=get(ENV,"SLURM_STEP_ID","0")
println("=== compute.jl $jobid $stepid")

## Load data
d=JSON.parsefile("compute.json")
hr=convert(Array{Float64},d["HR"])
sh=convert(Array{Float64},d["SH"])

## Compute regression HR ~ SH

## Build y, X [c, SH]
n=length(hr)
y=sh
x=hcat(ones(n,1),hr)

## Solve for beta hat (coefficients)
bh=inv(x'*x)*(x'*y)
println("+++ ",bh)

## Write results
result=Dict("bh0"=> bh[1],"bh1"=>bh[2])
f=open("result-$jobid-$stepid.json","w")
JSON.print(f,result)
close(f)

