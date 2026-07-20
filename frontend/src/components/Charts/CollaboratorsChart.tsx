import {
    BarChart,
    Bar,
    ResponsiveContainer,
    XAxis,
    Tooltip
} from "recharts";

const data = [
    { gestor: "Pablo", total: 45 },
    { gestor: "Clóvis", total: 38 },
    { gestor: "Alyf", total: 52 },
    { gestor: "Welliton", total: 47 }
];

export default function CollaboratorsChart() {
    return (
        <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
                <XAxis dataKey="gestor" />
                <Tooltip />
                <Bar
                    dataKey="total"
                    fill="#F97316"
                    radius={[6, 6, 0, 0]}
                />
            </BarChart>
        </ResponsiveContainer>
    );
}