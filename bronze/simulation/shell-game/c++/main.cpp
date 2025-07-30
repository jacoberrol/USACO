#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <boost/algorithm/string.hpp>

using namespace std;

int main() {
    ifstream stream = ifstream("shell.in");

    string line;
    string contents;

    while (getline(stream, line)) {
        contents.append(line + "\n");
    }

    vector<string> lines;

    boost::split(lines, contents, boost::is_any_of("\n"));

    int count = atoi(lines.at(0).c_str());

    int shells[] = {0, 1, 2};
    int counts[] = {0, 0, 0};

    for (int i = 1; i < (count + 1); i++) {

        line = lines.at(i);
        vector<string> values;
        boost::split(values, line, boost::is_any_of(" "));

        int a = atoi(values[0].c_str()) - 1;
        int b = atoi(values[1].c_str()) - 1;
        int g = atoi(values[2].c_str()) - 1;

        int old = shells[a];
        shells[a] = shells[b];
        shells[b] = old;

        counts[shells[g]]++;
    }

    int m = counts[0];

    for (int i = 1; i < 3; i++) {
        if (m < counts[i]) {
            m = counts[i];
        }
    }

    ofstream out = ofstream("shell.out");

    out << m;
}