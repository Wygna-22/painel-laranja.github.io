import {
    PieChart,
    Pie,
    Cell,
    ResponsiveContainer,
    Tooltip,
    Legend,
} from "recharts";

interface Props {
    ativos: number;
    afastados: number;
    desligados: number;
}

const COLORS = [
    "#22C55E",
    "#F97316",
    "#EF4444",
];

export default function StatusChart({
    ativos,
    afastados,
    desligados,
}: Props) {

    const data = [
        {
            name: "Ativos",
            value: ativos,
        },
        {
            name: "Afastados",
            value: afastados,
        },
        {
            name: "Desligados",
            value: desligados,
        },
    ];

    return (
        <ResponsiveContainer width="100%" height="100%">
            <PieChart>

                <Pie
                    data={data}
                    dataKey="value"
                    innerRadius={60}
                    outerRadius={90}
                >
                    {data.map((_, index) => (
                        <Cell
                            key={index}
                            fill={COLORS[index]}
                        />
                    ))}
                </Pie>

                <Tooltip />
                <Legend />

            </PieChart>
        </ResponsiveContainer>
    );
}