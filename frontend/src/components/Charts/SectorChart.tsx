import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Tooltip,
    Legend,
    Cell,
} from "recharts";

interface Props{

    data:{
        setor:string;
        quantidade:number;
    }[];

}

const COLORS=[
    "#F97316",
    "#FDBA74",
    "#FB923C",
    "#EA580C",
    "#C2410C",
];

export default function SectorChart({data}:Props){

    return(

        <ResponsiveContainer width="100%" height="100%">

            <PieChart>

                <Pie
                    data={data}
                    dataKey="quantidade"
                    nameKey="setor"
                    innerRadius={60}
                    outerRadius={90}
                >

                    {data.map((_,index)=>(

                        <Cell
                            key={index}
                            fill={COLORS[index%COLORS.length]}
                        />

                    ))}

                </Pie>

                <Tooltip/>

                <Legend/>

            </PieChart>

        </ResponsiveContainer>
    );
}