import {
    PieChart,
    Pie,
    Cell,
    ResponsiveContainer
} from "recharts";

const data = [
    { name: "Ativos", value: 150 },
    { name: "Férias", value: 12 },
    { name: "Folga", value: 20 }
];

const COLORS = [
    "#F97316",
    "#22C55E",
    "#3B82F6"
];

export default function StatusChart() {

    return (

        <ResponsiveContainer width="100%" height="100%">

            <PieChart>

                <Pie
                    data={data}
                    innerRadius={60}
                    outerRadius={90}
                    dataKey="value"
                >

                    {data.map((_, index) => (
                        <Cell
                            key={index}
                            fill={COLORS[index]}
                        />
                    ))}

                </Pie>

            </PieChart>

        </ResponsiveContainer>

    );

}