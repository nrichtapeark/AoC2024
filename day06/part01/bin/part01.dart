import 'dart:io';
import 'dart:math';

const NORTH = Point(0, -1);
const SOUTH = Point(0, 1);
const EAST = Point(1, 0);
const WEST = Point(-1, 0);

bool try_step(List<String> grid, Point guard, Point direction) {
    var new_guard = guard + direction;

    var contents = grid[new_guard.y.toInt()][new_guard.x.toInt()];

    if (contents == '#')
        return false;

    grid[new_guard.y.toInt()] = grid[new_guard.y.toInt()].replaceRange(new_guard.x.toInt(), new_guard.x.toInt()+1, "X");

    return true;
}

void main(List<String> arguments) async {
    var dataFile = new File(arguments[0]);
    var guard = Point(-1, -1);
    List<String> grid = [];

    var lines = await dataFile.readAsLines();

    lines.forEach((line) {
        for (int i = 0; i< line.length; i++) {
            if (line[i] == '^') {
                guard = Point(i, grid.length);
            }
        }
        grid.add(line);
    });

    var direction = NORTH;

    try {
        while (true) {
            if (!try_step(grid, guard, direction)) {
                if (direction == NORTH) {
                    direction = EAST;
                } else if (direction == EAST) {
                    direction = SOUTH;
                } else if (direction == SOUTH) {
                    direction = WEST;
                } else if (direction == WEST) {
                    direction = NORTH;
                }
            } else {
                guard += direction;
            }
        }
    } on RangeError catch (e) {
        // Out of bounds
    }

    var sum = 0; 
    grid.forEach((line) {
        sum += 'X'.allMatches(line).length;
    });

    print(sum);
}
