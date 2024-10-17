module euler

using Dates

function save_benchmark(p, b)
    file = "benchmarks_jl.csv"
    if !isfile(file)
        touch(file)
        open(file, "w") do f
            write(f, "Problem,Date,Julia\n")
            write(f, "$p,$(Dates.today()),$(sum(b.times)/length(b.times))\n")
        end
    else
        open(file, "a") do f
            write(f, "$p,$(Dates.today()),$(sum(b.times)/length(b.times))\n")
        end
    end
end

end # module
