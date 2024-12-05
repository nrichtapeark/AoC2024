import Foundation
import ArgumentParser

@main
struct Part01: ParsableCommand {
    @Option(help: "Specify the input")
    public var input: String

    public func run() throws {
        let contents = try! String(contentsOfFile: input, encoding: String.Encoding.utf8)
        let lines = contents.split { $0.isNewline }

        var rules: [(Int, Int)] = []

        var sum: Int = 0

        for line in lines {
            let input = String(line)

            if input.count == 5 {
                let rule = input.split(separator: "|")
                let a: Int? = Int(rule[0])
                let b: Int? = Int(rule[1])

                rules.append((a!, b!))
            } else {
                var pages: [Int] = []

                for idx in input.split(separator: ",") {
                    let page_idx = Int(idx)!
                    pages.append(page_idx)
                }

                var valid: Bool = true
                var previous: Int = pages[0]

                for idx in 1...pages.count-1 {
                    let page = pages[idx]

                    for rule in rules {
                        if previous == rule.1 && page == rule.0 {
                            valid = false
                            break
                        }
                    }

                    if !valid {
                        break
                    }

                    previous = page;
                }

                if valid {
                    sum += pages[pages.count/2]
                }
            }
        }

        print(sum)
    }
}


