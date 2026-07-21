import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

interface Props {
    data: {
        mes: string;
        quantidade: number;
    }[];
}

export default function VacationChart({ data }: Props) {
    return (
        <ResponsiveContainer width="100%" height="100%">
            <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="mes" />
                <YAxis />
                <Tooltip />
                <Line
                    type="monotone"
                    dataKey="quantidade"
                    stroke="#F97316"
                    strokeWidth={3}
                />
            </LineChart>
        </ResponsiveContainer>
    );
}